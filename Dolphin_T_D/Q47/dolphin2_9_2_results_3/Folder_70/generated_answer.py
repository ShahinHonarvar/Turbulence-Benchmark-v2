def palindromes_of_specific_lengths(s):
    s = s[10:70].lower()
    palindromes = set()
    length = 0
    for i in range(len(s)):
        if s[i].isalpha():
            length += 1
            j = i + 1
            while j < len(s) and (j - i + 1 <= 52 or j - i + 1 == 24):
                if not s[j].isalpha():
                    i = j
                    length = 0
                    break
                j += 1
                length += 1
            if j - i + 1 >= 24 and j - i + 1 <= 52:
                string = s[i:j]
                if string == string[::-1]:
                    palindromes.add(string)
    return palindromes