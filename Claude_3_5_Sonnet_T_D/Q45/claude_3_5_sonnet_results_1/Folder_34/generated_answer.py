def palindromes_between_indices(s):
    letters = [c for c in s[5:8].lower() if c.isalpha()]

    def generate_palindromes(chars, current='', result=set()):
        if len(current) >= 4 and current == current[::-1]:
            result.add(current)
        if chars:
            for i, char in enumerate(chars):
                generate_palindromes(chars[:i] + chars[i + 1:], current + char, result)
        return result
    return generate_palindromes(letters)