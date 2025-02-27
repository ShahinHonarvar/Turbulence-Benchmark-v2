def palindromes_of_specific_lengths(s):
    substring = s[127:289]
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 119, min(i + 141, len(substring)) + 1):
            sub = substring[i:j]
            if all((x.isalpha() for x in sub)) and sub.replace('a', 'A').replace('e', 'E').replace('i', 'I').replace('o', 'O').replace('u', 'U').replace('y', 'Y') == sub.replace('A', 'a').replace('E', 'e').replace('I', 'i').replace('O', 'o').replace('U', 'u').replace('Y', 'y')[::-1]:
                palindromes.add(sub.replace('a', 'A').replace('e', 'E').replace('i', 'I').replace('o', 'O').replace('u', 'U').replace('y', 'Y'))
    return palindromes