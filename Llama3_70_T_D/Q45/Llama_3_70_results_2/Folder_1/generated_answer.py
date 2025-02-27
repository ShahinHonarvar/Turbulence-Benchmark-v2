def palindromes_between_indices(s):
    letters = [c.lower() for c in s[4:8] if c.isalpha()]
    letters_set = set(letters)
    palindromes = set()
    for p1 in letters_set:
        for p2 in letters_set:
            for p3 in letters_set:
                for p4 in letters_set:
                    for p5 in letters_set:
                        palindrome = p1 + p2 + p3 + p4 + p5
                        if palindrome == palindrome[::-1] and len(palindrome) >= 5:
                            palindromes.add(palindrome)
    return palindromes