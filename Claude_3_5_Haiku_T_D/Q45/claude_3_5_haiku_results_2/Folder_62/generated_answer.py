def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]

    def get_letter_counts(substr):
        return {char.lower(): substr.lower().count(char) for char in set(substr.lower()) if char.isalpha()}
    substr = s[:9]
    letter_counts = get_letter_counts(substr)
    palindromes = set()
    for length in range(7, len(substr) + 1):
        for chars in [char.lower() for char in substr if char.isalpha()]:
            current_counts = letter_counts.copy()
            candidate_palindrome = []
            for i in range(length // 2):
                if current_counts.get(chars, 0) > 0:
                    candidate_palindrome.append(chars)
                    current_counts[chars] -= 2
                else:
                    break
            if len(candidate_palindrome) == length // 2:
                middle = chars if length % 2 == 1 and current_counts.get(chars, 0) > 0 else ''
                full_palindrome = ''.join(candidate_palindrome + [middle] + candidate_palindrome[::-1])
                if len(full_palindrome) >= 7 and is_palindrome(full_palindrome):
                    palindromes.add(full_palindrome)
    return palindromes