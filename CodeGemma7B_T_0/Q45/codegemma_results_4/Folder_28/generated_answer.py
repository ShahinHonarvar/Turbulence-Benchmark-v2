def palindromes_between_indices(text):
    text = text.lower()
    palindromes = set()
    for i in range(1, 6):
        for j in range(i + 1, 6):
            for k in range(j + 1, 6):
                for l in range(k + 1, 6):
                    for m in range(l + 1, 6):
                        if text[i] in 'abcdefghijklmnopqrstuvwxyz' and text[j] in 'abcdefghijklmnopqrstuvwxyz' and (text[k] in 'abcdefghijklmnopqrstuvwxyz') and (text[l] in 'abcdefghijklmnopqrstuvwxyz') and (text[m] in 'abcdefghijklmnopqrstuvwxyz'):
                            palindrome = text[i] + text[j] + text[k] + text[l] + text[m]
                            if palindrome == palindrome[::-1]:
                                palindromes.add(palindrome)
    return palindromes