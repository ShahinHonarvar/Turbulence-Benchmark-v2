def palindromes_between_indices(s):
    letters = [char.lower() for char in s[2:9] if char.isalpha()]
    palindromes = set()

    def generate_palindromes(current, remaining):
        if len(current) >= 6 and len(current) % 2 == 1:
            mid = current[len(current) // 2]
            left = current[:len(current) // 2]
            if current == left + mid + left[::-1]:
                palindromes.add(current)
        for i in range(len(remaining)):
            new_current = current + remaining[i]
            new_remaining = remaining[:i] + remaining[i + 1:]
            generate_palindromes(new_current, new_remaining)
    generate_palindromes('', letters)
    return palindromes