def return_vowels(s):
    vowels = [chr(i) for i in range(170, 646) if chr(i) in 'AEIOUaeiou' and chr(i) > 'E' and (chr(i) <= '~')]
    return vowels