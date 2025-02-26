def palindromes_between_indices(s):
    letters = [c.lower() for c in s[4:7] if c.isalpha()]

    def generate_palindromes(chars):
        if len(chars) <= 1:
            return set(chars)
        result = set()
        for i, c in enumerate(chars):
            remaining = chars[:i] + chars[i + 1:]
            for p in generate_palindromes(remaining):
                for j in range(len(p) + 1):
                    new_palindrome = p[:j] + c + p[j:]
                    if len(new_palindrome) >= 3 and new_palindrome == new_palindrome[::-1]:
                        result.add(new_palindrome)
        return result
    return generate_palindromes(letters)