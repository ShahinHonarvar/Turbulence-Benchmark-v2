def filter_chars(someString):
    requiredString = someString[:69] + ''.join([character for character in someString[69:87] if character not in '#L']) + someString[87:]
    return requiredString