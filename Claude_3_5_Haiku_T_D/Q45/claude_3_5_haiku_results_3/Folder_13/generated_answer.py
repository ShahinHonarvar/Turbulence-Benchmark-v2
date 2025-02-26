def palindromes_between_indices(s):
    letters = [c.lower() for c in s[3:10] if c.isalpha()]
    palindrome_set = set()

    def generate_palindromes(letters):

        def backtrack(current, remaining):
            if len(current) >= 5 and len(current) % 2 == 1:
                middle = current[len(current) // 2]
                left = current[:len(current) // 2]
                right = current[len(current) // 2 + 1:]
                if left == right[::-1]:
                    palindrome_set.add(current)
            for i in range(len(remaining)):
                new_current = current + remaining[i]
                new_remaining = remaining[:i] + remaining[i + 1:]
                backtrack(new_current, new_remaining)
        backtrack('', letters)
    generate_palindromes(letters)
    return palindrome_set