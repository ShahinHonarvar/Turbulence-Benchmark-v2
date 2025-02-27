def palindromes_between_indices(s):
    substring = s[0:7]
    lad_an = [x for x in substring if x.isalpha()]
    palind = set()
    for i in range(len(lad_an)):
        for j in range(i + 2, len(lad_an) + 1):
            temp_str = ''.join(lad_an[i:j])
            temp_str = temp_str.lower()
            if temp_str == temp_str[::-1]:
                palind.add(temp_str)
    return palind