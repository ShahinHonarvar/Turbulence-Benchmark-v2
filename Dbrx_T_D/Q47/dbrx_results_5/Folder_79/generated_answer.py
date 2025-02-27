def palindromes_of_specific_lengths(s):
    s = s.lower()
    palindromes = set()
    for i in range(1, 9):
        for j in range(len(s) - i + 1):
            substring = s[j:j + i]
            if i == len(substring) == 3 or i == len(substring) == 4:
                if substring[0] not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
                    continue
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes