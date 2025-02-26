def palindromes_between_indices(s):
    letters_range = ''.join((c.lower() for c in s[5:7] if c.isalpha()))
    if len(letters_range) < 3:
        return set()

    def generate_palindromes(chars):

        def backtrack(current_palindrome, remaining_chars):
            if len(current_palindrome) >= 3 and current_palindrome == current_palindrome[::-1]:
                palindrome_set.add(current_palindrome)
            for i in range(len(remaining_chars)):
                new_palindrome = current_palindrome + remaining_chars[i]
                new_remaining = remaining_chars[:i] + remaining_chars[i + 1:]
                backtrack(new_palindrome, new_remaining)
        palindrome_set = set()
        backtrack('', chars)
        return palindrome_set
    return generate_palindromes(letters_range)