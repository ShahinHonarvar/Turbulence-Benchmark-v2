def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for i, char in enumerate(s[202:872]) if char in vowels and 3 < ord(char) <= 126]
    return result