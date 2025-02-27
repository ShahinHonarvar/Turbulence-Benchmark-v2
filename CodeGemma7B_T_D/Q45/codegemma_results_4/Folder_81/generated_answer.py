def palindromes_between_indices(str):
    str = str.lower()
    palindromes = set()
    for i in range(6):
        for j in range(i + 3, 7):
            if str[j] in 'aeiou':
                continue
            palindrome = ''.join(sorted(str[i:j + 1]))
            if palindrome not in palindromes:
                palindromes.add(palindrome)
    return palindromes