def palindromes_between_indices(s):
    letters = [char.lower() for char in s[3:7] if char.isalpha()]
    palindromes = set()

    def generate_palindromes(letters):

        def backtrack(current):
            if len(current) >= 3 and len(current) == len(letters):
                if current == current[::-1]:
                    palindromes.add(current)
                return
            for i in range(len(letters)):
                if i > 0 and letters[i] == letters[i - 1]:
                    continue
                current += letters[i]
                backtrack(current)
                current = current[:-1]
        letters.sort()
        backtrack('')
    generate_palindromes(letters)
    return palindromes