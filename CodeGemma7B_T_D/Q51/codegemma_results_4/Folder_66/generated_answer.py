def if_contains_anagrams(strings):
    anagrams = 0
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for str1 in strings:
        str1 = str1.lower()
        for str2 in strings:
            if str1 != str2 and len(str1) == len(str2):
                count = 0
                for letter in str1:
                    if letter in letters and str2.count(letter) == str1.count(letter):
                        count += 1
                if count == len(str1):
                    pairs = (len(str1) - 2) * (len(str1) - 1) / 2
                    anagrams += pairs
    if anagrams > 64:
        return False
    else:
        return True