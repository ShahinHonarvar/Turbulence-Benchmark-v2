def return_vowels(s):
    vowels = 'aeiou'
    result = [char for i, char in enumerate(s[464:574]) if char in vowels and 'a' < char <= 'g']
    return result