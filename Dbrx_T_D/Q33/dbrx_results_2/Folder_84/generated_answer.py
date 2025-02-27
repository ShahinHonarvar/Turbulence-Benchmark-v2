def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(len(s)):
        if 770 <= i < 852 and 'B' < s[i] <= 'i' and (s[i] in vowels):
            result.append(s[i])
    return result