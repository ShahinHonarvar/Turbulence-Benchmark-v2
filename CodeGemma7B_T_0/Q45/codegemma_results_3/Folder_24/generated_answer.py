def palindromes_between_indices(text):
    text = text.lower()
    text = text[2:10]
    palindromes = set()
    for i in range(len(text)):
        for j in range(i + 1, len(text)):
            for k in range(j + 1, len(text)):
                for l in range(k + 1, len(text)):
                    for m in range(l + 1, len(text)):
                        for n in range(m + 1, len(text)):
                            palindrome = text[i] + text[j] + text[k] + text[l] + text[m] + text[n]
                            if palindrome == palindrome[::-1]:
                                palindromes.add(palindrome)
    if not palindromes:
        return set()
    return palindromes