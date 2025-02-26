def palindromes_between_indices(s):
    substring = s[4:9].lower()
    letters = [char for char in substring if char.isalpha()]

    def generate_palindromes(chars):

        def backtrack(current, remaining):
            if len(current) >= 6 and len(current) % 2 == 1:
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