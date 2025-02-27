from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[433]
    ans = []
    for i in range(x):
        if isprime(i) and (not str(i).count('0')) and isprime(int(str(i)[1:])) and isprime(int(str(i)[2:])) and isprime(int(str(i)[3:])) and isprime(int(str(i)[4:])) and isprime(int(str(i)[5:])) and isprime(int(str(i)[6:])) and isprime(int(str(i)[7:])) and isprime(int(str(i)[8:])) and isprime(int(str(i)[9:])) and isprime(int(str(i)[10:])) and isprime(int(str(i)[11:])) and isprime(int(str(i)[12:])) and isprime(int(str(i)[13:])) and isprime(int(str(i)[14:])) and isprime(int(str(i)[15:])) and isprime(int(str(i)[16:])) and isprime(int(str(i)[17:])) and isprime(int(str(i)[18:])) and isprime(int(str(i)[19:])) and isprime(int(str(i)[20:])) and isprime(int(str(i)[21:])) and isprime(int(str(i)[22:])) and isprime(int(str(i)[23:])) and isprime(int(str(i)[24:])) and isprime(int(str(i)[25:])) and isprime(int(str(i)[26:])) and isprime(int(str(i)[27:])) and isprime(int(str(i)[28:])) and isprime(int(str(i)[29:])) and isprime(int(str(i)[30:])) and isprime(int(str(i)[31:])) and isprime(int(str(i)[32:])) and isprime(int(str(i)[33:])) and isprime(int(str(i)[34:])) and isprime(int(str(i)[35:])) and isprime(int(str(i)[36:])) and isprime(int(str(i)[37:])) and isprime(int(str(i)[38:])) and isprime(int(str(i)[39:])) and isprime(int(str(i)[40:])) and isprime(int(str(i)[41:])) and isprime(int(str(i)[42:])) and isprime(int(str(i)[43:])):
            ans.append(i)
    return sorted(ans, reverse=True)