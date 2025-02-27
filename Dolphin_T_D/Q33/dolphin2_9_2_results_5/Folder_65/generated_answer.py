def return_vowels(S):
    vowels = 'aeiou'
    result = []
    for char in S[71:88]:
        if 9 < ord(char) <= 80 and char.lower() in vowels:
            result.append(char)
    return result