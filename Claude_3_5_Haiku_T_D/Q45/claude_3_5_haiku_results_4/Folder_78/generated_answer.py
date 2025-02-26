def palindromes_between_indices(s):
    substring = s[6:9].lower()
    letters = [char for char in substring if char.isalpha()]

    def can_form_palindrome(letter_list):
        letter_counts = {}
        for letter in letter_list:
            letter_counts[letter] = letter_counts.get(letter, 0) + 1
        odd_count = sum((1 for count in letter_counts.values() if count % 2 != 0))
        return odd_count <= 1

    def generate_palindromes(letter_list):
        if not can_form_palindrome(letter_list):
            return set()

        def backtrack(path, remaining):
            if not remaining:
                if len(path) >= 3:
                    return {path}
                return set()
            result = set()
            for i in range(len(remaining)):
                if i > 0 and remaining[i] == remaining[i - 1]:
                    continue
                new_remaining = remaining[:i] + remaining[i + 1:]
                result.update(backtrack(path + remaining[i], new_remaining))
                result.update(backtrack(remaining[i] + path, new_remaining))
            return result
        all_palindromes = set()
        letters_sorted = sorted(letter_list)
        for palindrome in backtrack('', letters_sorted):
            if palindrome == palindrome[::-1]:
                all_palindromes.add(palindrome)
        return all_palindromes
    return generate_palindromes(letters)