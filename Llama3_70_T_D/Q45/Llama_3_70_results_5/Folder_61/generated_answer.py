def palindromes_between_indices(s):
    s = s[:8].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 7, len(letters) + 1):
            sub = letters[i:j]
            if len(sub) >= 7:
                first_half = ''.join(sub[:len(sub) // 2])
                second_half = ''.join(sub[len(sub) // 2 + len(sub) % 2:][::-1])
                if first_half == second_half:
                    palindrome = ''.join(sub)
                    palindromes.add(palindrome)
    return palindromes