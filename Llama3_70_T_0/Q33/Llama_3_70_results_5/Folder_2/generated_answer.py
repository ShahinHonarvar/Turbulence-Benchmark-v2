def return_vowels(s):
    vowels = [chr(i) for i in range(170, 646) if chr(i) > 'E' and chr(i) <= '~' and (chr(i) in 'AEIOUaeiou')]
    return vowels