def palindromes_between_indices(str):
    str = str.lower()
    palindromes = set()
    for first in range(26):
        for second in range(first, 26):
            for third in range(second, 26):
                word = chr(first + ord('a')) + chr(second + ord('a')) + chr(third + ord('a'))
                if word[0] in str[5:7] and word[1] in str[5:7] and (word[2] in str[5:7]):
                    palindromes.add(word)
    return palindromes