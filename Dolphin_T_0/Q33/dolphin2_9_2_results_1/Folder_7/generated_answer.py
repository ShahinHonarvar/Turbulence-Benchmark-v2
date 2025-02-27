def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    answer = []
    for char in s[202:872]:
        if 3 < ord(char) <= ord('>'):
            if char in vowels:
                answer.append(char)
    return answer