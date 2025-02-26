def palindromes_between_indices(s):
    letters = [c.lower() for c in s[4:8] if c.isalpha()]
    palindromes = set()

    def generate_palindromes(current_perm, remaining_letters):
        if len(current_perm) >= 4 and len(current_perm) % 2 == 0:
            if current_perm == current_perm[::-1]:
                palindromes.add(current_perm)
        for i in range(len(remaining_letters)):
            new_perm = current_perm + remaining_letters[i]
            new_remaining = remaining_letters[:i] + remaining_letters[i + 1:]
            generate_palindromes(new_perm, new_remaining)
    generate_palindromes('', letters)
    return palindromes