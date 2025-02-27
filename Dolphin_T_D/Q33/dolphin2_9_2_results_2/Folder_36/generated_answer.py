def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    res = []
    for i in range(604, 949):
        if i < len(string):
            ch = string[i]
            if ch > 'N' and ch <= 'U' and (ch in vowels):
                res.append(ch)
    return res