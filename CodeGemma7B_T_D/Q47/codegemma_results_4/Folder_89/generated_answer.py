def palindromes_of_specific_lengths(str1):
    pali = set()
    for i in range(len(str1)):
        if i >= 18 and len(str1) - i >= 12:
            for l in range(12, 15):
                if str1[i:i + l] == str1[i + l - 1:i:-1].lower():
                    pali.add(str1[i:i + l].lower())
    return pali