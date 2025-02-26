def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[1:6])).lower()

    def generate_palindromes(chars):
        if len(chars) <= 1:
            return set(chars)
        result = set()
        for i, c in enumerate(chars):
            rest = chars[:i] + chars[i + 1:]
            for p in generate_palindromes(rest):
                for j in range(len(p) + 1):
                    new_p = p[:j] + c + p[j:]
                    if len(new_p) >= 4 and new_p == new_p[::-1]:
                        result.add(new_p)
        return result
    return generate_palindromes(letters)