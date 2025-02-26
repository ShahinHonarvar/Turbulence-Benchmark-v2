def palindromes_between_indices(s):
    letters = [c.lower() for c in s[:3] if c.isalpha()]

    def generate_palindromes(chars):

        def backtrack(current, remaining):
            if len(current) >= 3 and len(current) % 2 == 1:
                mid = len(current) // 2
                if ''.join(current[:mid]) == ''.join(current[mid + 1:][::-1]):
                    palindromes.add(''.join(current))
            for i in range(len(remaining)):
                current.append(remaining[i])
                backtrack(current, remaining[:i] + remaining[i + 1:])
                current.pop()
        palindromes = set()
        backtrack([], chars)
        return palindromes
    return generate_palindromes(letters)