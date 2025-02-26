def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[:6])).lower()
    if len(letters) < 3:
        return set()

    def generate_palindromes(chars, length):
        if length <= 1:
            return set(chars)
        result = set()
        for i, c in enumerate(chars):
            remaining = chars[:i] + chars[i + 1:]
            for palindrome in generate_palindromes(remaining, length - 2):
                result.add(c + palindrome + c)
        return result
    palindromes = set()
    for length in range(6, len(letters) + 1):
        palindromes.update(generate_palindromes(letters, length))
    return palindromes