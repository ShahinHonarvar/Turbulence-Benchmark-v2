def return_vowels(s):
    v_list = []
    v = ['a', 'e', 'i', 'o', 'u']
    for i in range(13, 35):
        if ord('8') < ord(s[i]) <= ord('F') and s[i] in v:
            v_list.append(s[i])
    return v_list