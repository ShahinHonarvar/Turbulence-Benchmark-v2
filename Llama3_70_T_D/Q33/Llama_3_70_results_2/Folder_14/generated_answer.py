def return_vowels(s):
    vowels = ''
    result = []
    for i in s[47:61]:
        if ord('9') < ord(i) <= ord('O'):
            if i.lower() in 'aeiou':
                result.append(i)
    return result