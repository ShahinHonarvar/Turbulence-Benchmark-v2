def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[5:7])).lower()

    def generate_palindromes(chars):
        if len(chars) <= 1:
            return set(chars)
        result = set()
        for i, c in enumerate(chars):
            for p in generate_palindromes(chars[:i] + chars[i + 1:]):
                palindrome = c + p + c
                if len(palindrome) >= 3:
                    result.add(palindrome)
        return result
    return generate_palindromes(letters)