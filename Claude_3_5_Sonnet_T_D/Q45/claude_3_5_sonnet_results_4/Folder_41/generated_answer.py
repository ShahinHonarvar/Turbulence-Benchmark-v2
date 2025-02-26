def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[2:4])).lower()
    if len(letters) < 2:
        return set()

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(chars):
        if len(chars) <= 1:
            return set(chars)
        result = set()
        for i, c in enumerate(chars):
            rest = chars[:i] + chars[i + 1:]
            for p in generate_palindromes(rest):
                new_pal = c + p + c
                if len(new_pal) >= 3:
                    result.add(new_pal)
        return result
    return generate_palindromes(letters)