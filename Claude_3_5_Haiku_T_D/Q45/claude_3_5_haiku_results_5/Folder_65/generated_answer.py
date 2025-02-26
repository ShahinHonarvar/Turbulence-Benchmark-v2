def palindromes_between_indices(s):
    letters = [c.lower() for c in s[:7] if c.isalpha()]
    palindromes = set()

    def generate_palindromes(letters):

        def backtrack(current, remaining):
            if len(current) >= 5 and len(current) == 2 * (len(current) // 2):
                if current == current[::-1]:
                    palindromes.add(current)
            for i in range(len(remaining)):
                backtrack(current + remaining[i], remaining[:i] + remaining[i + 1:])
        backtrack('', letters)
    generate_palindromes(letters)
    return palindromes