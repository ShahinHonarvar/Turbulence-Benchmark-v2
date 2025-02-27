def return_vowels(s):
    if 10 <= len(s) <= 97:
        result = []
        for char in s[10:97]:
            if char in 'aeiouAEIOU' and 'R' < char <= 'b':
                result.append(char)
        if len(result) == 0:
            return []
        return result