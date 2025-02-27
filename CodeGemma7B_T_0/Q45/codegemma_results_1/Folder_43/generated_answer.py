def palindromes_between_indices(text):
    text = text.lower()
    palindromes = set()
    for i in range(2, 6):
        for j in range(i + 1, 6):
            for k in range(j + 1, 6):
                for l in range(k + 1, 6):
                    for m in range(l + 1, 6):
                        palindrome = text[i] + text[j] + text[k] + text[l] + text[m]
                        if palindrome == palindrome[::-1]:
                            palindromes.add(palindrome)
    return palindromes