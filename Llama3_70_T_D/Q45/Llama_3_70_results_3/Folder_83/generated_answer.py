def palindromes_between_indices(s):
    s = s[2:10].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for r in range(7, 8 + len(letters) // 2):
        for p in itertools.combinations_with_replacement(letters, r):
            first_half = ''.join(p)
            second_half = first_half[::-1]
            palindrome = first_half + second_half
            if len(palindrome) >= 7:
                palindromes.add(palindrome)
            if len(palindrome) < 7 and len(palindrome) % 2 == 1:
                for c in letters:
                    new_palindrome = first_half + c + second_half
                    if new_palindrome not in palindromes:
                        palindromes.add(new_palindrome)
    return palindromes