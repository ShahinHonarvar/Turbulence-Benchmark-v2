def palindromes_between_indices(s):
    letters = [char.lower() for char in s[5:9] if char.isalpha()]
    palindromes = set()

    def generate_palindromes(letters):

        def backtrack(current, remaining):
            if len(current) >= 3 and len(current) == len(letters):
                if current == current[::-1]:
                    palindromes.add(current)
                return
            for i in range(len(remaining)):
                backtrack(current + remaining[i], remaining[:i] + remaining[i + 1:])
        backtrack('', letters)
    generate_palindromes(letters)
    return palindromes