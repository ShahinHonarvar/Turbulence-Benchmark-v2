def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:4] if c.isalpha()]
    if len(letters) < 3:
        return set()

    def generate_palindromes(chars):

        def backtrack(current, remaining):
            if len(current) >= 3 and len(current) % 2 == 1:
                mid = len(current) // 2
                if current[:mid] == current[mid + 1:][::-1]:
                    palindromes.add(current)
            for i in range(len(remaining)):
                new_current = current + remaining[i]
                new_remaining = remaining[:i] + remaining[i + 1:]
                backtrack(new_current, new_remaining)
        palindromes = set()
        backtrack('', chars)
        return palindromes
    return generate_palindromes(letters)