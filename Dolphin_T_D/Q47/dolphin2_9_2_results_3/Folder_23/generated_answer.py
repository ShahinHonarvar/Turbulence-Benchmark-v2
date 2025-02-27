def palindromes_of_specific_lengths(s):
    substring = s[23:95]
    palindromes = set()
    for i in range(23, 95):
        for j in range(i + 17, 95):
            sub = substring[i:j + 1]
            lower_sub = sub.lower()
            if lower_sub == lower_sub[::-1] and set(sub).issubset({'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}):
                palindromes.add(sub)
    return palindromes