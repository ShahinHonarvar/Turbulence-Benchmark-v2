def palindromes_between_indices(s):
    substring = s[3:9].lower()
    letters = [char for char in substring if char.isalpha()]
    if len(letters) < 5:
        return set()

    def generate_palindromes(chars):

        def backtrack(current_perm, remaining_chars):
            if len(current_perm) > len(chars):
                return set()
            palindromes = set()
            if len(current_perm) >= 5 and current_perm == current_perm[::-1]:
                palindromes.add(current_perm)
            for i in range(len(remaining_chars)):
                new_perm = current_perm + remaining_chars[i]
                new_remaining = remaining_chars[:i] + remaining_chars[i + 1:]
                palindromes.update(backtrack(new_perm, new_remaining))
            return palindromes
        return backtrack('', chars)
    return generate_palindromes(letters)