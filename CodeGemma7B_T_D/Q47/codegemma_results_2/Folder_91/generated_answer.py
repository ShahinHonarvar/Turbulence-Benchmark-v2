def palindromes_of_specific_lengths(str):
    palindromes = set()
    for i in range(0, 11):
        for j in range(i + 1, 11):
            if str[i] == str[j]:
                if 3 <= j - i + 1 <= 5:
                    palindrome = str[i:j + 1].lower()
                    if palindrome not in palindromes:
                        palindromes.add(palindrome)
    return palindromes