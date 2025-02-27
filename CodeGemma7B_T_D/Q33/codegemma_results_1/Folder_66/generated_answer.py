def return_vowels(str):
    return list((ch for ch in str[63:79] if ch.lower() in 'aeiou' and ord(ch.lower()) > ord('d') and (ord(ch.lower()) <= ord('y'))))