def palindromes_between_indices(s):
    sub_string = s[7:10].lower()
    letters = [c for c in sub_string if c.isalpha()]
    palindromes = set()
    if len(letters) < 2:
        return palindromes
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            first = letters[i]
            second = letters[j]
            if first == second:
                palindrome = first * 2
                if len(palindrome) >= 4:
                    palindromes.add(palindrome)
            else:
                palindrome = first + second + second + first
                if len(palindrome) >= 4:
                    palindromes.add(palindrome)
    return palindromes