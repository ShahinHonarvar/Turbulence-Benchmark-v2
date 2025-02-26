def palindromes_between_indices(s):
    letters = [char.lower() for char in s[2:5] if char.isalpha()]
    if len(letters) < 3:
        return set()

    def generate_palindromes(current, remaining):
        if len(current) >= 3 and len(remaining) == 0:
            if current == current[::-1]:
                return {current}
            return set()
        palindromes = set()
        for i in range(len(remaining)):
            new_current = current + remaining[i]
            new_remaining = remaining[:i] + remaining[i + 1:]
            palindromes.update(generate_palindromes(new_current, new_remaining))
            palindromes.update(generate_palindromes(remaining[i] + current, new_remaining))
        return palindromes
    return generate_palindromes('', letters)