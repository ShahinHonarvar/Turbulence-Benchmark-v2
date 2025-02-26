def palindromes_between_indices(s):
    letters = [c.lower() for c in s[7:10] if c.isalpha()]

    def generate_palindromes(chars, current='', result=set()):
        if len(current) >= 4 and current == current[::-1]:
            result.add(current)
        if len(chars) > 0:
            for i, char in enumerate(chars):
                generate_palindromes(chars[:i] + chars[i + 1:], current + char, result)
                generate_palindromes(chars[:i] + chars[i + 1:], char + current, result)
        return result
    return generate_palindromes(letters)