def palindromes_between_indices(s):
    letters = [char.lower() for char in s[4:8] if char.isalpha()]
    palindrome_set = set()

    def generate_palindromes(current, remaining):
        if len(current) >= 5 and len(current) == 2 * (len(current) // 2):
            if current == current[::-1]:
                palindrome_set.add(current)
        for i in range(len(remaining)):
            new_current = current + remaining[i]
            new_remaining = remaining[:i] + remaining[i + 1:]
            generate_palindromes(new_current, new_remaining)
    generate_palindromes('', letters)
    return palindrome_set