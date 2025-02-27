def palindromes_between_indices(text):
    text = text.lower()
    text = text[2:6]
    palindromes = set()
    for i in range(len(text)):
        for j in range(i + 1, len(text)):
            for k in range(j + 1, len(text)):
                for l in range(k + 1, len(text)):
                    for m in range(l + 1, len(text)):
                        palindrome = text[i] + text[j] + text[k] + text[l] + text[m]
                        if palindrome == palindrome[::-1]:
                            palindromes.add(palindrome)
    return palindromes